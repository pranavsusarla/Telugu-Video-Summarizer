<template>
    <div>
    <div v-if="!loading">
        <form class="container w-50" @submit.prevent>
            <label for="url" class="form-label">YouTube URL: </label>
            <input type="text" name="url" v-model="url" class="form-control">
            <button class="btn btn-danger m-2" @click="submitURL">Summarize!</button>
        </form>
    </div>
    <div v-else>
        Generating Transcript from URL...
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
                loading: false
            }
        },

        methods:{
            async submitURL(){
                if(this.url != ''){
                    this.loading=true;
                    console.log(this.url);
                    // send url to backend and generate summary via fetch calls
                    const data = {'url': this.url}
                    const response = await fetch(apiurl,{
                        method: 'POST',
                        headers:{
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data)
                    })
                    const json =  await response.json()
                    console.log(json);

                    this.$router.push('/summary');
                }else{
                    alert('You entered an empty URL!')
                }
            }
        }
    }
</script>

<style scoped>

</style>