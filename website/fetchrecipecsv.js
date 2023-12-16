
    // Replace 'your-github-username' and 'your-repo' with yourGitHub username and repository name
    const csvUrl2 = 'https://raw.githubusercontent.com/DarrellOwensRCD/detailed-census-2020/master/DetailedCensus/DetailedCensus2020/recipes_dic.csv';

    // Function to fetch and process the CSV file
    async function fetchrecipeCSV() {
      try {
        const response = await fetch(csvUrl2);
        const csvData = await response.text();

        // Split the CSV data into rows
        const rows = csvData.split('\n');
        // Remove headers
        rows.shift();
        // Array to store list items
        const dataDictionary = {};

        // Iterate through rows and create dictionary pairs
        rows.forEach(row => {
          const arr= row.split(",");
          const key= String(arr[0]);
          const value= String(arr[1]);
          // Add the key-value pair to the dictionary
          dataDictionary[key] = value;
        });
        return dataDictionary;
      } catch (error) {
        console.error('Error fetching or processing CSV:', error);
        return NULL;
      }
    }