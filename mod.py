import os
import logging
import openai

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configure OpenAI API key
openai.api_key = 'your-api-key-here'  # Replace with your actual OpenAI API key

def generate_tests_for_file(file_path):
    """
    Function to generate test cases for a given Python file using OpenAI Codex (GPT-4).
    
    :param file_path: Path to the Python file.
    :return: None
    """
    logging.info(f"Generating test cases for {file_path}")
    
    try:
        # Read the content of the Python file
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Use OpenAI API to generate test cases (you may need to modify the prompt)
        response = openai.Completion.create(
            engine="gpt-4",  # Or use another engine if necessary
            prompt=f"Generate test cases for the following Python code without any markdown formatting:\n\n{file_content}",
            max_tokens=150,  # Adjust as needed for the test case length
            temperature=0.5,
        )
        
        test_cases = response.choices[0].text.strip()

        # Clean up the generated text by removing any unwanted markdown formatting (if any)
        test_cases = test_cases.replace("```python", "").replace("```", "").strip()

        # Manually create the import statement based on the filename (without '.py')
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        import_statement = f"from {file_name} import *"  # This should now dynamically adjust to the file name

        # Add the import statement at the beginning of the generated test cases
        test_cases = import_statement + "\n\n" + test_cases
        
        # Ensure the 'tests' directory exists
        if not os.path.exists('tests'):
            os.makedirs('tests')

        # Save the generated test cases to a new file in the 'tests' directory
        test_file_name = f"test_{os.path.basename(file_path)}"
        with open(os.path.join('tests', test_file_name), 'w') as test_file:
            test_file.write(test_cases)
        
        logging.info(f"✅ AI-generated test cases for {file_path} saved in tests/{test_file_name}")
    
    except Exception as e:
        logging.error(f"Error generating test cases for {file_path}: {e}")

def process_directory(directory_path):
    """
    Function to process all Python files in a directory and generate test cases for each file.
    
    :param directory_path: Path to the directory containing Python files.
    :return: None
    """
    logging.info(f"Processing directory: {directory_path}")
    
    try:
        # List all Python files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".py"):  # Only process Python files
                file_path = os.path.join(directory_path, filename)
                generate_tests_for_file(file_path)
        
    except Exception as e:
        logging.error(f"Error processing directory {directory_path}: {e}")
