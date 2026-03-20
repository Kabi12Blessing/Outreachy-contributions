import csv
import requests

# I used two libraries:
# csv - to read the input file containing the URLs
# requests - to visit each URL and get its response status code

# This list will store every result so I can save them to a file later
results = []


with open('Task 2 - Intern.csv', 'r') as file:
    reader = csv.reader(file)

    # The first row is just the column name "urls", so I skip it
    next(reader)

    # Going through the file one URL at a time
    for row in reader:

        # Cleaning extra spaces around the URL
        url = row[0].strip()

        # Only processing the row if it actually has a URL in it
        if url:
            try:
                # Visit the URL
                # wait 5 seconds to connect, 10 seconds to get a response
                response = requests.get(url, timeout=(5, 10))

                # Format and print the result
                line = f"({response.status_code}) {url}"
                print(line)

                # Then saving it to the results list
                results.append(line)

            # If the server took too long to respond
            except requests.exceptions.Timeout:
                line = f"(TIMEOUT) {url}"
                print(line)
                results.append(line)

            # If the URL is completely unreachable (for instance, dead link, no internet, etc)
            except requests.exceptions.ConnectionError:
                line = f"(CONNECTION ERROR) {url}"
                print(line)
                results.append(line)

            # Catch any other unexpected errors
            except Exception as e:
                line = f"(ERROR) {url}"
                print(line)
                results.append(line)

# After checking all URLs, save everything to a text file

with open('task2_results.txt', 'w') as output_file:
    output_file.write('\n'.join(results))

print("\nDone! Results saved to task2_results.txt")
