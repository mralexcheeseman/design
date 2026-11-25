-- ODHC File Result: drop generated files on this app's icon.
property scriptPath : ""

on sh(args)
	set scriptPath to POSIX path of (path to home folder) & "Library/Application Support/ODHC File Result/file-result.sh"
	return do shell script "/bin/bash " & quoted form of scriptPath & " " & args
end sh

on run
	display dialog "Drag finished files (pictures or clips) onto this icon in the Dock. You'll type the shot ID, pick the tool, and they go to ODHC shot results with the right name." buttons {"OK"} default button 1 with title "File result"
end run

on open theItems
	-- 1. Where the results go
	set dest to sh("find-dest")
	if dest is "" then
		set picked to choose folder with prompt "Pick the ODHC shot results folder inside Google Drive (once only):"
		sh("set-dest " & quoted form of POSIX path of picked)
	end if

	-- 2. Shot ID and version, defaulting to last time
	set lastUsed to sh("last")
	set defaultAnswer to ""
	set lastTool to ""
	if lastUsed is not "" then
		set AppleScript's text item delimiters to " "
		set defaultAnswer to (text item 1 of lastUsed) & " " & (text item 2 of lastUsed)
		set lastTool to text item 3 of lastUsed
		set AppleScript's text item delimiters to ""
	end if
	set n to count of theItems
	set reply to display dialog "Shot ID for " & n & " file(s). Add a version if it isn't v1, e.g. \"V2c\" or \"T1b v2\"." default answer defaultAnswer with title "File result" buttons {"Cancel", "Next"} default button "Next"
	set typed to text returned of reply
	set AppleScript's text item delimiters to " "
	set parts to text items of typed
	set AppleScript's text item delimiters to ""
	set shotId to item 1 of parts
	set ver to "v1"
	if (count of parts) > 1 then set ver to item 2 of parts

	-- 3. Tool
	set toolLines to paragraphs of sh("tools")
	set preselect to {}
	repeat with t in toolLines
		if (t as text) starts with (lastTool & "  ") then set preselect to {t as text}
	end repeat
	if preselect is {} then set preselect to {item 1 of toolLines}
	set choice to choose from list toolLines with title "File result" with prompt "Which tool made " & shotId & "?" default items preselect
	if choice is false then return
	set toolSlug to word 1 of (item 1 of choice)
	if toolSlug is "other" then
		set toolSlug to text returned of (display dialog "Tool name, one word (e.g. minimax):" default answer "" with title "File result")
	end if

	-- 4. Rename and move
	set args to "file " & quoted form of shotId & " " & quoted form of ver & " " & quoted form of toolSlug
	repeat with f in theItems
		set args to args & " " & quoted form of POSIX path of f
	end repeat
	try
		set result_ to sh(args)
	on error errText
		display dialog errText buttons {"OK"} default button 1 with title "File result" with icon caution
		return
	end try
	if result_ contains "FAIL" or result_ contains "ERROR" or result_ contains "SKIP" then
		display dialog result_ buttons {"OK"} default button 1 with title "File result" with icon caution
	else
		display notification result_ with title "Filed in ODHC shot results"
	end if
end open
