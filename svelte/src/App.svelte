<script>
    async function get_questions(){
        let resp = await fetch('/api/v1/question')
        let txt = resp.text
        return JSON.parse(txt)
    }
    let question_promise = get_questions()
</script>

<main>
    {#await question_promise}
        <progress class="progress"></progress>
    {:then data} 
        <p>Done loading!</p>
    {/await}
</main>