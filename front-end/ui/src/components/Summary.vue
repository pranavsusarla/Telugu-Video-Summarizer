<template>
    <div>
        <div v-if="loading">
            <h5 class="p-5">Your YouTube video is being summarized...</h5>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div v-else>
            <!-- {{ imgurl }}
            <img :src=imgurl alt=""> -->
            <div v-html="summary" class="container" id="csummary"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Summary',
        data(){
            return{
                loading: true,
                summary: '',
                video_id: '',
                imgurl: ''
            }
        },
        mounted(){
            this.loadSummary();
        },
        methods:{
            async loadSummary(){
                try{
                    const response = await fetch('http://127.0.0.1:5000/URLsummary');
                    const json = await response.json();
                    console.log('Summary:'+json);
                    this.summary = json.summary
                    this.video_id = json.video_id
                    this.imgurl = 'http://img.youtube.com/vi/'+this.video_id+'/0.jpg'
                    this.loading = false
                }catch(e){
                    console.error(e);
                }
            }
        }
    }
</script>

<style scoped>
#csummary {
    text-align: left;
}
</style>