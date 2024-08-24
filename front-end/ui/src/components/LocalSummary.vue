<template>
    <div>
        <div v-if="loading">
            <h5 class="p-5">Your Local video is being summarized...</h5>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div v-else>
            <div class="container">
                <button class="btn btn-primary m-3" @click="language='english'">English</button>
                <button class="btn btn-success m-3" @click="language='telugu'">Telugu</button>
                <button class="btn btn-danger m-3" @click="language='hindi'">Hindi</button>
            </div>
            <!-- {{ imgurl }}
            <img :src=imgurl alt=""> -->
            <div v-html="summary" class="container" id="csummary"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'LocalSummary',
        data(){
            return{
                loading: true,
                summary: '',
                language: 'english'
            }
        },
        mounted(){
            this.loadSummary();
        },
        methods:{
            async loadSummary(){
                try{
                    const response = await fetch('http://127.0.0.1:5000/localSummary');
                    const json = await response.json();
                    console.log('JSON FROM LSUMMARY: '+json.summary);
                    this.summary = json.summary;
                    this.loading = false
                }catch(e){
                    console.error(e);
                }
            }
        }
    }
</script>

<style scoped>

</style>