import requests
import pandas as pd
import io

class SDW:
    def __init__(self, flowRef, key, startDate, endDate):
        self.flowRef = flowRef
        self.key = key
        self.startDate = startDate      # Format must be YYYY-MM-DD
        self.endDate = endDate      # Format must be YYYY-MM-DD

    def setup(self):
        entrypoint = 'https://sdw-wsrest.ecb.europa.eu/service/'  # Using protocol 'https'
        resource = 'data'  # The resource for data queries is always'data'
        flowRef = self.flowRef  # Dataflow describing the data that needs to be returned, exchange rates in this case
        key = self.key  # Defining the dimension values, explained below

        # Define the parameters
        parameters = {
            'startPeriod': self.startDate,
            'endPeriod': self.endDate
        }

        # Construct full size URL
        request_url = entrypoint + resource + '/' + flowRef + '/' + key

        # Make a request
        response = requests.get(request_url, params=parameters, headers={'Accept': 'text/csv'})

        # Read the response as a file into a Pandas DataFrame
        df = pd.read_csv(io.StringIO(response.text))

        # Making Sure everything is visiblw
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        ts = df.filter(['TIME_PERIOD', 'OBS_VALUE'], axis=1)

        # 'TIME_PERIOD' was of type 'object' (as seen in df.info). Convert it to datetime first
        ts['TIME_PERIOD'] = pd.to_datetime(ts['TIME_PERIOD'])

        # Set 'TIME_PERIOD' as index
        ts = ts.set_index('TIME_PERIOD')

        return ts

