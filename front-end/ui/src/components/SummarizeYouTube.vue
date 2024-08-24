<template>
    <div>
    <div v-if="!loading && error=='' ">
        <form class="container w-50" @submit.prevent>
            <label for="url" class="form-label">YouTube URL: </label>
            <input type="text" name="url" v-model="url" class="form-control">
            <button class="btn btn-danger m-2" @click="submitURL">Summarize!</button>
        </form>
    </div>
    <div v-if="loading && error==''">
        <h5 class="p-5">Generating Transcript from URL...</h5>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
    </div>
    <div v-if="error!=''">
        <h3 class="p-5 text-danger">{{ error }}</h3>
    </div>
    </div>
</template>

<script>
    const apiurl="http://127.0.0.1:5000/URLsummary"

    export default {
        name: 'SummarizeYouTube',
        data(){
            return{
                url: '',
                loading: false,
                error: ''
            }
        },

        methods:{
            async submitURL(){
                if(this.url != ''){
                    this.loading=true;
                    console.log(this.url);
                    // send url to backend and generate summary via fetch calls
                    const data = {'url': this.url}
                    try{
                        const response = await fetch(apiurl,{
                            method: 'POST',
                            body: JSON.stringify(data)
                        })
                        const json =  await response.json()
                        console.log(json);

                        this.$router.push('/summary');
                    }catch(e){
                        this.loading = false;
                        this.error = 'There seems to be a problem in fetching the URL. Please try again after some time'
                        console.error(e);
                    }
                }else{
                    alert('You entered an empty URL!')
                }
            }
        }
    }
</script>

<style scoped>

</style>