# Grape Jelly

Grape Jelly is a Python application that monitors directories for new video files and normalizes their audio using FFmpeg. The application uses environment variables for configuration and can be run in a Docker container.

## Features

- Monitors specified directories for new video files
- Normalizes audio using FFmpeg with customizable settings
- Supports multiple video and audio codecs
- Configurable via environment variables

## Requirements

- Python 3.7+
- Docker
- Docker Compose

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/grape-jelly.git
    cd grape-jelly
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Create a `.env` file with the following content:
    ```properties
    AUDIO_CODEC=eac3
    AUDIO_BITRATE=256k
    SAMPLE_RATE=48000
    LOUDNESS_TARGET=-24.0
    TRUE_PEAK=-2.0
    LOUDNESS_RANGE_TARGET=6.0
    VIDEO_CODEC=libx265
    DIRECTORIES_TO_WATCH=path/to/your/directory
    ```

## Usage

### Running Locally

1. Activate the virtual environment:
    ```sh
    source venv/bin/activate
    ```

2. Run the application:
    ```sh
    python src/main.py
    ```

### Running with Docker

1. Build the Docker image:
    ```sh
    docker-compose build
    ```

2. Run the application:
    ```sh
    docker-compose up
    ```

## Configuration

The application can be configured using the following environment variables:

- `AUDIO_CODEC`: The audio codec to use (default: `aac`)
- `AUDIO_BITRATE`: The audio bitrate (default: `192k`)
- `SAMPLE_RATE`: The sample rate (default: `48000`)
- `LOUDNESS_TARGET`: The loudness target (default: `-24.0`)
- `TRUE_PEAK`: The true peak (default: `-2.0`)
- `LOUDNESS_RANGE_TARGET`: The loudness range target (default: `7.0`)
- `VIDEO_CODEC`: The video codec to use (default: `libx264`)
- `DIRECTORIES_TO_WATCH`: Comma-separated list of directories to watch for new video files

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
