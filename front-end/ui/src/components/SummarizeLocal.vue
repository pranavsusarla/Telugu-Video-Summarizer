<template>
    <div>
        <form class="container w-50" @submit.prevent>
            <label class="form-label" for="customFile">Upload Local File</label>
            <input type="file" class="form-control" id="customFile" @change="handleFileUpload" />
            <button class="btn btn-danger" @click="uploadFile">Upload File</button>

            <button v-if="isFileUploaded" class="btn btn-danger m-2">Summarize!</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'SummarizeLocal',
        data(){
            return{
                selectedFile: null,
                isFileUploaded: false
            }
        },
        methods:{
            handleFileUpload(event){
                this.selectedFile = event.target.files[0];
            },
            uploadFile(){
                if (!this.selectedFile) {
                    alert('Please select a file first!');
                    return;
                }

                const formData = new FormData();
                formData.append('file', this.selectedFile);

                fetch('http://127.0.0.1:5000/uploadFile', {
                    method: 'POST',

                    body: formData,
                })
                .then(response => console.log(response))
                .then(data => {
                    console.log('Success:', data);
                    alert('File uploaded successfully!');
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to upload file.');
                });

                this.$router.push('/summaryLocal');
            }
        }
    }
</script>

<style scoped>

</style>