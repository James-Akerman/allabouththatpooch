// Get the data
d3.json("/data").then(function(data){
    // console.log(data[0]);

    // Populate Arrays
    let breed=[]
    let male_min = []
    let male_max = []
    let female_min = []
    let female_max = []
    let urls = []
    let male_size = []
    let female_size = []

    for (i in data){
        breed.push(data[i]['Breed'])
        male_min.push(data[i]['Weight_Male_Min'])
        male_max.push(data[i]['Weight_Male_Max'])
        female_min.push(data[i]['Weight_Female_Min'])
        female_max.push(data[i]['Weight_Female_Max'])
        urls.push(data[i]['Url'])
        male_size.push(data[i]['Size_Male'])
        female_size.push(data[i]['Size_Female'])
    }

});


d3.json("/ftop10").then(function(data){
    // Populate Arrays
    let breed=[]
    let female_max = []
    for (i in data){
        breed.push(data[i]['Breed'])
        female_max.push(data[i]['Weight_Female_Max'])
    }
    let trace1 = {
        x: female_max,
        y: breed,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: '#ff0000'
        }
      };
      let data_weight = [trace1];
      let layout = {
        title:'Top 10 Female Breeds by Maximum Weight'
      };   
      Plotly.newPlot('weight_top_female', data_weight, layout);
});

d3.json("/fbottom10").then(function(data){
    // Populate Arrays
    let breed=[]
    let female_max = []
    for (i in data){
        breed.push(data[i]['Breed'])
        female_max.push(data[i]['Weight_Female_Max'])
    }
    let trace1 = {
        x: female_max,
        y: breed,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: '#ffbf00'
        }
      };
      let data_weight = [trace1];
      let layout = {
        title:'Bottom 10 Female Breeds by Maximum Weight'
      };   
      Plotly.newPlot('weight_bottom_female', data_weight, layout);
});

d3.json("/mtop10").then(function(data){
    // Populate Arrays
    let breed=[]
    let male_max = []
    for (i in data){
        breed.push(data[i]['Breed'])
        male_max.push(data[i]['Weight_Male_Max'])
    }
    let trace1 = {
        x: male_max,
        y: breed,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: '#0000ff'
        }
      };
      let data_weight = [trace1];
      let layout = {
        title:'Top 10 Male Breeds by Maximum Weight'
      };   
      Plotly.newPlot('weight_top_male', data_weight, layout);
});

d3.json("/mbottom10").then(function(data){
    // Populate Arrays
    let breed=[]
    let male_max = []
    for (i in data){
        breed.push(data[i]['Breed'])
        male_max.push(data[i]['Weight_Male_Max'])
    }
    let trace1 = {
        x: male_max,
        y: breed,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: '#00ffff'
        }
      };
      let data_weight = [trace1];
      let layout = {
        title:'Bottom 10 Male Breeds by Maximum Weight'
      };   
      Plotly.newPlot('weight_bottom_male', data_weight, layout);
});




