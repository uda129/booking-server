build:
	docker build -t booking_server:latest .

run:
	docker run --name booking_server -d -p 80 booking_server:latest