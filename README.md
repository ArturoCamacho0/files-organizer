# Downloads Organizer

A Python script to organize files in the Downloads folder by moving them to designated folders based on file types. Configuration is managed using a .env file.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/downloads-organizer.git
   cd downloads-organizer
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory with the following content:
   ```dotenv
   DOWNLOADS_FOLDER=C:\\Users\\yourusername\\Downloads
   DOCUMENTS_FOLDER=C:\\Users\\yourusername\\OneDrive\\Documentos
   PICTURES_FOLDER=C:\\Users\\yourusername\\OneDrive\\Imágenes
   VIDEOS_FOLDER=C:\\Users\\yourusername\\OneDrive\\Videos
   ```

5. Run the script:
   ```sh
   python organize_downloads.py
   ```
