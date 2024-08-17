<template>
    <div>
        <form class="container w-50" @submit.prevent>
            <label class="form-label" for="customFile">Upload Local File</label>
            <input type="file" class="form-control" id="customFile" />
            <button class="btn btn-danger m-2" @click="submitURL">Summarize!</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'SummarizeLocal'
    }
</script>

<style scoped>

</style>