build:
	docker build -t booking_server:latest .

stop:
	docker stop booking_server
	docker rm booking_server

run:
	docker run --name booking_server -d -p 8000:80 booking_server:latest