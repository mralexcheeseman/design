-- ODHC File Result: drop generated pictures or clips on this app's icon.
-- A local model (Ollama) guesses each file's shot; you confirm with one click.

on sh(args)
	set scriptPath to POSIX path of (path to home folder) & "Library/Application Support/ODHC File Result/file-result.sh"
	return do shell script "/bin/bash " & quoted form of scriptPath & " " & args
end sh

on splitTabs(t)
	set AppleScript's text item delimiters to tab
	set parts to text items of t
	set AppleScript's text item delimiters to ""
	return parts
end splitTabs

on run
	display dialog "Drag finished pictures or clips (or a whole folder) onto File Result in the Dock. It guesses each one's shot, you confirm, and it files them in ODHC shot results with the right name." buttons {"OK"} default button 1 with title "File result"
end run

-- Ask for shot ID, version and tool by hand. Returns {id, ver, tool} or missing value.
on askByHand(fileName, defId, defTool)
	set reply to display dialog "Shot ID for " & fileName & ". Add a version if it isn't v1, e.g. \"V2c\" or \"T1b v2\"." default answer defId with title "File result" buttons {"Skip", "Next"} default button "Next"
	if button returned of reply is "Skip" then return missing value
	set AppleScript's text item delimiters to " "
	set parts to text items of (text returned of reply)
	set AppleScript's text item delimiters to ""
	set shotId to item 1 of parts
	set ver to "v1"
	if (count of parts) > 1 then set ver to item 2 of parts
	set toolLines to paragraphs of sh("tools")
	set preselect to {item 1 of toolLines}
	repeat with t in toolLines
		if (t as text) starts with (defTool & "  ") then set preselect to {t as text}
	end repeat
	set choice to choose from list toolLines with title "File result" with prompt "Which tool made " & shotId & "?" default items preselect
	if choice is false then return missing value
	set toolSlug to word 1 of (item 1 of choice)
	if toolSlug is "other" then set toolSlug to text returned of (display dialog "Tool name, one word (e.g. minimax):" default answer "" with title "File result")
	return {shotId, ver, toolSlug}
end askByHand

on open theItems
	if sh("find-dest") is "" then
		set picked to choose folder with prompt "Pick the ODHC shot results folder inside Google Drive (once only):"
		sh("set-dest " & quoted form of POSIX path of picked)
	end if

	-- Folders dropped in count as their files.
	set fileList to {}
	repeat with f in theItems
		set p to POSIX path of f
		if p ends with "/" then
			set found to paragraphs of (do shell script "find " & quoted form of p & " -maxdepth 1 -type f ! -name '.*' | sort")
			repeat with g in found
				if (g as text) is not "" then set end of fileList to (g as text)
			end repeat
		else
			set end of fileList to p
		end if
	end repeat

	set lastTool to ""
	set lastUsed to sh("last")
	if lastUsed is not "" then set lastTool to do shell script "printf %s " & quoted form of lastUsed & " | awk '{print $3}'"

	set total to count of fileList
	set done to {}
	set progress total steps to total
	repeat with i from 1 to total
		set p to item i of fileList
		set fileName to do shell script "basename " & quoted form of p
		set progress completed steps to i - 1
		set progress description to "Looking at " & fileName & " (" & i & " of " & total & ")"
		do shell script "qlmanage -p " & quoted form of p & " >/dev/null 2>&1 & echo $! > /tmp/odhc-ql.pid"
		set g to splitTabs(sh("guess " & quoted form of p))
		set gId to item 1 of g
		set gConf to item 2 of g
		set gTool to item 3 of g
		set gShot to item 4 of g
		if gTool is "" then set gTool to lastTool
		set pick to missing value
		if gId is not "" and gTool is not "" then
			set newName to sh("name " & quoted form of gId & " v1 " & quoted form of gTool & " " & quoted form of p)
			set how to gConf & "% sure"
			if gConf is "100" then set how to "from its name"
			set msg to "File " & i & " of " & total & ": " & fileName & return & return & "Looks like " & gId & " (" & how & "): " & gShot & return & return & "Will be filed as:" & return & newName
			activate
			set reply to display dialog msg with title "File result" buttons {"Skip", "Change...", "File it"} default button "File it"
			if button returned of reply is "File it" then
				set pick to {gId, "v1", gTool}
			else if button returned of reply is "Change..." then
				set pick to askByHand(fileName, gId, gTool)
			end if
		else
			activate
			set pick to askByHand(fileName, gId, gTool)
		end if
		do shell script "kill $(cat /tmp/odhc-ql.pid) >/dev/null 2>&1; rm -f /tmp/odhc-ql.pid; true"
		if pick is not missing value then
			set lastTool to item 3 of pick
			try
				set r to sh("file " & quoted form of (item 1 of pick) & " " & quoted form of (item 2 of pick) & " " & quoted form of (item 3 of pick) & " " & quoted form of p)
			on error errText
				set r to "FAIL: " & errText
			end try
			set end of done to r
		end if
	end repeat

	set AppleScript's text item delimiters to return
	set summary to done as text
	set AppleScript's text item delimiters to ""
	if summary is "" then return
	if summary contains "FAIL" or summary contains "ERROR" then
		display dialog summary buttons {"OK"} default button 1 with title "File result" with icon caution
	else
		display notification summary with title "Filed in ODHC shot results"
	end if
end open
