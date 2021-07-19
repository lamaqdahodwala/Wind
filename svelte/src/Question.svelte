<script>
    export let pk;
    async function load_question(){
        let resp = await fetch(`/api/v1/question/${pk}`)
        let json = resp.json()
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
                <hr>
                <p class="content">
                    {data.body}
                </p>
            </div>
        </div>
    {/await}
</main>