# certHistory
`certHistory` is a command-line tool that retrieves certificate history for a given domain name by querying the crt.sh website. 

## Usage

To use certHistory, follow these steps:

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the `certHistory.py` file.
3. Run the following command

    ```bash
    python certHistory.py [Domain] [Count]
    or
    python certHistory.py [Domain]
    ```

    - Replace `Domain` with the target domain name that you want to retrieve certificate history for.
    - Replace `Count` with the number of certificates you want to retrieve (Optional). By default, the tool retrieves the 5 most recent certificates. If the count is too high, the site may temporarily block you.
    
4. Wait for the tool to complete. The tool will retrieve the certificate history for the specified domain name by querying the crt.sh website and display the results.



## Requirements

certHistory requires Python 3 and the following packages:

- `requests`

To install the required packages, run the following command:

```bash
pip install requests
```
Tested on Linux

![Alt text](Screenshot.jpeg?raw=true "Screenshot")

## Contributing

If you find any issues with the `certHistory` or would like to contribute to the project, please feel free to submit a pull request or open an issue on the Github repository.

## License
`certHistory` is licensed under the [Creative Commons Attribution-NonCommercial (CC BY-NC) license](https://creativecommons.org/licenses/by-nc/4.0/).

