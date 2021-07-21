<script>
    export let pk;
    let name;
    async function load_question(){
        let resp = await fetch(`/api/v1/question/${pk}`)
        let json = await resp.json()
        return json
    }
</script>

<main>
    {#await load_question()}
        <progress class="progress"></progress>
    {:then data}
        <div class="container">
            <div class="box is-fluid">
                <h1 class="title">{data.title}</h1>
                <h1 class="subtitle">Written by {data.op.username}</h1>
                <hr>
                <p class="content">
                    {data.body}
                </p>
            </div>
            <hr>
            <div class="has-text-centered">
                <h1 class="title">Answers</h1>
            </div>
            {#each data.answers as i}
                <div class="box is-fluid">
                    <p class="content">
                        {i.body}
                    </p>
                    <br>
                    Written by {i.user.username}
                </div>
            {:else}
                <div class="has-text-centered">
                    <p>No answers yet</p>
                </div>
            {/each}
        </div>
    {:catch error}
        <p>{error}</p>
    {/await}
</main>