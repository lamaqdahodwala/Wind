<script>
    import {send_gql_request} from './assets/assets.js'
    import {queries} from './assets/queries.js'
    async function load_questions(){
        
        let resp = await send_gql_request(queries.all_questions)
        return resp['data']
    }
</script>

<div class='container'>
    {#await load_questions()}
        <progress class="progress"></progress>
    {:then data} 
        {#each data['allQuestions'] as i}
            <div class="card">
                <div class="card-header">
                    <h1 class="card-header-title title">{i.title}</h1>
                </div>
                <div class="card-content">
                    <div class="content">
                        {i.body}
                    </div>
                </div>
            </div>
            <br><br>
        {/each}
    {/await}
</div>