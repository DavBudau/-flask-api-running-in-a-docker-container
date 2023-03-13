This is an example of a flask rest api running in a docker container. Database used is SQlite. Data type: video games.

Requirements https://www.docker.com/products/docker-desktop/

Usage

Run docker-compose:

docker-compose up --build

Test localhost api in your browser by navigating to: http://localhost:5000/get_data?data_type=video_games&snippet=false

NOTE:'snippet=false' means all data will be shown 'snippet=true' means first 20 pieces of data will be shown
