
    // Replace 'your-github-username' and 'your-repo' with yourGitHub username and repository name
    const csvUrl = 'https://raw.githubusercontent.com/DarrellOwensRCD/detailed-census-2020/master/DetailedCensus/DetailedCensus2020/EthnicGroupsWithAssociatedCounties.csv';

    // Function to fetch and process the CSV file
    async function fetchcountyCSV() {
      try {
        const response = await fetch(csvUrl);
        const csvData = await response.text();

        // Split the CSV data into rows
        const rows = csvData.split('\n');
        // Remove headers
        rows.shift();
        rows.shift();
        rows.shift();
        // Array to store list items
        const dataDictionary = {};

        // Iterate through rows and create dictionary pairs
        rows.forEach(row => {
          const key = String(row.substring(0, 4));
          // The data is formatted backwards, unfortunately for JSON parsing
          const valueString = row.replace(/"/g, '').replace(/'/g, '"').substring(5).trim();
          if (valueString.length > 0){
            const value = JSON.parse(valueString);
            // Add the key-value pair to the dictionary
            dataDictionary[String(key)] = value;
          }
        });
        return dataDictionary;
      } catch (error) {
        console.error('Error fetching or processing CSV:', error);
        return NULL;
      }
    }