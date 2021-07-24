<script>
    import {send_gql_request} from './assets/assets.js'
    async function load_questions(){
        let resp = await send_gql_request(
`{
    allQuestions{
        title
        body
    }
}`)
        let json = resp.json()
        return json['data']
    }
</script>

<div>
    {#await load_questions()}
        <progress class="progress"></progress>
    {:then data} 
        {#each data['allQuestions'] as i}
            <div class="card">
                <h1 class="card-title">{i.title}</h1>
                <div class="card-content">
                    <div class="content">
                        {i.body}
                    </div>
                </div>
            </div>
        {/each}
    {/await}
</div>