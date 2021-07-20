<script>
    async function get_questions(){
        let resp = await fetch('/api/v1/question')
        let txt = resp.json()
        return txt
    }
</script>

<main>
    {#await get_questions()}
        <progress class="progress"></progress>
    {:then data} 
        <div class="container">
            {#each data.reverse() as i}
                <div class="card">
                    <div class="card-header">
                        <a href="/question/{i.id}" class="card-header-title title">{i.title}</a>
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