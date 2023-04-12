on run {input, parameters}
	set myText to (item 1 of input) as text

	-- Replace newline characters with spaces
	set AppleScript's text item delimiters to {linefeed, return}
	set myTextItems to text items of myText
	set AppleScript's text item delimiters to " "
	set myText to myTextItems as text
	set AppleScript's text item delimiters to ""

	set apiUrl to "https://api.elevenlabs.io/v1/text-to-speech/MF3mGyEYCl7XYWbV9V6O/stream"
	set apiKey to "YOUR_ELEVENLABS_API_KEY_HERE"

	set jsonPayload to "{\"text\":\"" & myText & "\",\"voice_settings\":{\"stability\":0.75,\"similarity_boost\":0.75}}"

	set curlCommand to "curl -s -X 'POST' \\" & linefeed & "'" & apiUrl & "' \\" & linefeed & "-H 'accept: */*' \\" & linefeed & "-H 'xi-api-key: " & apiKey & "' \\" & linefeed & "-H 'Content-Type: application/json' \\" & linefeed & "--data-binary @- <<< " & (quoted form of jsonPayload)

	set ffmpegCommand to "| /opt/homebrew/bin/ffmpeg -i pipe:0 -f mp3 - | /opt/homebrew/bin/ffplay -autoexit -nodisp -hide_banner -loglevel panic -"

	do shell script curlCommand & ffmpegCommand

	return input
end run