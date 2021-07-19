<script>
    async function get_questions(){
        let resp = await fetch('/api/v1/question')
        let txt = resp.json()
        return txt
    }
    let question_promise = get_questions()
</script>

<main>
    {#await question_promise}
        <progress class="progress"></progress>
    {:then data} 
        <div class="container">
            {#each data as i}
                <div class="card">
                    <div class="card-header">
                        <h1 class="card-header-title title">{i.title}</h1>
                    </div>
                    <div class="card-content">
                        <p class="content">
                            {i.body}
                        </p>
                    </div>
                </div>
                <br><br>
            {/each}
        </div>
    {:catch error}
        <div class="container has-text-centered">
            <p>{error}</p>
        </div>
    {/await}
</main>