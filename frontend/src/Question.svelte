<script>
    import { send_gql_request } from './assets/assets.js'
    import { queries } from './assets/queries.js'

    export let pk
    let answer_content;

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
                <p>Written by <a href='/user/{data.user.id}'>{data.user.username}</a></p>
            </div>
        </div>
        <br>
        <div class="has-text-centered">
            <h1 class="title is-2">Answers</h1>
        </div>
        <hr>
        {#each data.answers as i}
            <div class="box is-fluid">
                <div class="content">
                    {i.content}
                    <br><br>
                    written by <a href='/user/{i.user.id}'>{i.user.username}</a>
                </div>
            </div>
            <br><br>
        {:else}
            <div class="has-text-centered">
                <h1 class="subtitle">No answers yet.</h1>
            </div>
        {/each}
        <br><br>
        <h1 class="subtitle">Got an answer?</h1>
        <textarea bind:value={answer_content} cols="30" rows="5" class="textarea" placeholder="Answer here..."></textarea>
        <br>
        <button class="button is-info is-outlined">Post answer</button>
    </div>
{/await}
<br><br><br>