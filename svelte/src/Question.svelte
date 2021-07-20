<script>
    export let pk;
    let name;
    async function load_question(){
        let resp = await fetch(`/api/v1/question/${pk}`)
        let json = await resp.json()
        let get_username = await fetch(json['op'])
        let d = await get_username.json()
        name = d['username']
        
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
                <h1 class="subtitle">Written by {name}</h1>
                <hr>
                <p class="content">
                    {data.body}
                </p>
            </div>
        </div>
    {:catch error}
        <p>{error}</p>
    {/await}
</main>