echo "@echo off
echo Setting up TestSphere development environment...

:: Create Python virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install Python dependencies
pip install -r requirements.txt

:: Install Node.js dependencies
cd frontend
npm install
cd ..

echo Setup complete!" > setup.bat