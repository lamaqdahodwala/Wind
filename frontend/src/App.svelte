<script>
    import {send_gql_request} from './assets/assets.js'
    import {queries} from './assets/queries.js'
    async function load_questions(){
        
        let resp = await send_gql_request(queries.all_questions)
        return resp['data']
    }
</script>

<div>
    {#await load_questions()}
        <progress class="progress"></progress>
    {:then data} 
        <p class="help">nice</p>
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