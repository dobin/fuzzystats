#!/bin/bash


i=0
while true; do
	curl --request PUT -H \"Content-Type: application/json\" --data "{\"id\": 1, \"start_time\": \"2018-10-05T10:30:45+02:00\", \"lastupdate_time\": \"2018-10-05T10:30:45+02:00\", \"iterations_per_sec\": 1, \"iterations_overall\": $i, \"crash_count\": 2, \"latest_crash\": \"2018-10-05T10:30:45+02:00\", \"path_count\": 1, \"latest_path\": \"2018-10-05T10:30:45+02:00\", \"title\": \"Test Fuzzing Run One\", \"text\": \"Meh\"}" http://localhost:8000/api/fuzzingruns/1/
	let i=i+1
	sleep 1
done
