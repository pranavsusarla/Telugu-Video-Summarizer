<template>
    <div class="d-flex justify-content-around m-5 p-5">
        <router-link to="/summarizeYoutube"><button class="btn btn-primary">Summarize from YouTube URL</button></router-link>
        <router-link to="/summarizeLocal"><button class="btn btn-success">Summarize from Local Files</button></router-link>
    </div>
</template>

<script>
    export default {
        name: 'HomePage',
        data(){
            return{
                
            }
        }
    }
</script>

<style scoped>

</style>