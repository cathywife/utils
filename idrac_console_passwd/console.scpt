on tapPassword(userName, Passwd)
    tell application "System Events"
        set theProcesses to application processes
        repeat with theProcess from 1 to count theProcesses
            set theName to (name of process theProcess)
            if theName contains "java" then
                tell process theProcess
                    try
                        set frontmost to true
                        repeat with x from 1 to (count windows)
                            set WindowName to name of window x
                            log WindowName
                            if WindowName contains "idrac" then
                                tell application "System Events" to tell process theProcess to perform action "AXRaise" of window x
                            end if
                            delay 1
                            
                            tell application "System Events" to keystroke userName
                            
                            tell application "System Events" to key code 36
                            delay 2
                            set keyCode to {29, 18, 19, 20, 21, 23, 22, 26, 28, 25}
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
                        end repeat
                    end try
                end tell
            end if
        end repeat
    end tell
end tapPassword
 
display dialog "Username: " default answer ""
set userName to text returned of result
display dialog "Password: " default answer ""
--- set password to text returned of result
tapPassword(userName, text returned of result)
