<script>
    import { send_gql_request } from './assets/assets.js'
    import { queries } from './assets/queries.js'

    export let pk

    async function load_question(){
        let resp = await send_gql_request(queries.single_question, {'pk': pk})
        return resp['data']['singleQuestion']
    }
</script>
<br><br>
{#await load_question()}
    <progress class="progress"></progress>
{:then data} 
    <div class="container">
        <div class="card">
            <div class="card-header">
                <h1 class="card-header-title title">{data.title}</h1>
            </div>
            <div class="card-content">
                {data.body}
                <br><br>
                <hr>
                <p>Written by <a>{data.user.username}</a></p>
            </div>
        </div>
        <div class="has-text-centered">
            <h1 class="title is-2">Answers</h1>
        </div>
    </div>
{/await}