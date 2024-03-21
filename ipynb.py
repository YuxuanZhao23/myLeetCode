import json

def create_ipynb_file(user_input):
    # Create a dictionary representing a Jupyter notebook
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# " + 
                    user_input + 
                    "\n =========Leetcode URL Link Placeholder========="
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [],
                "source": ["# Time Complexity: O()\n# Space Complexity: O()\n"]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    # Convert the notebook dictionary to JSON format
    notebook_json = json.dumps(notebook, indent=4)

    # Write the JSON data to a .ipynb file
    with open(user_input + ".ipynb", "w") as f:
        f.write(notebook_json)

if __name__ == "__main__":
    user_input = input("Enter LeetCode Question: ")
    create_ipynb_file(user_input)