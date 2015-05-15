set Passwd to "密码写在这里"
set keyCode to {29, 18, 19, 20, 21, 23, 22, 26, 28, 25}
delay 10
repeat with x from 1 to (length of Passwd)
	set ch to text item x of Passwd as string
	try
		set new_key to (ch as number) + 1
		set code to item new_key of keyCode
		tell application "System Events" to key code code
	on error errMsg
		set code to ch
		tell application "System Events" to keystroke ch
	end try
end repeat
tell application "System Events" to key code 36
