const ListRendering = {
    data() {
        return {
            suggestions: []
        }
    },
    mounted() {
        //get request
        //use results
        axios.get('/suggestions/')
            .then(function (response) {
                // handle success
                myapp.suggestions = response.data.suggestions;
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
        setInterval(()=>{
            axios.get('/suggestions/')
            .then(function (response) {
                // handle success
                myapp.suggestions = response.data.suggestions;
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
        }, 10000);

    }

}

myapp = Vue.createApp(ListRendering).mount('#list-rendering')