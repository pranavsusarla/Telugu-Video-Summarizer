<template>
    <div>
        <div v-if="loading">
            Your YouTube video is being summarized...
        </div>
        <div v-else v-html="summary" class="container" id="csummary"></div>
    </div>
</template>

<script>
    export default {
        name: 'Summary',
        data(){
            return{
                loading: true,
                summary: ''
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
                    console.log(json);
                    this.summary = json.summary
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