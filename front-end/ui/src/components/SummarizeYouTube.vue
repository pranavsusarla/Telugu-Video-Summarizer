<template>
    <div>
        <form class="container w-50">
            <label for="url" class="form-label">YouTube URL: </label>
            <input type="text" name="url" v-model="url" class="form-control">
            <button class="btn btn-danger m-2" @click="submitURL">Summarize!</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'SummarizeYouTube',
        data(){
            return{
                url: ''
            }
        },
        methods:{
            submitURL(){
                if(this.url != ''){
                    console.log(this.url);
                    // send url to backend and generate summary via fetch calls
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