<script>
    export let pk;
    import { getCookie } from './helpers/helpers.js'
    let answer_body;
    async function load_question(){
        let resp = await fetch(`/api/v1/question/${pk}`)
        let json = await resp.json()
        return json
    }
    async function send_answer(){
        if (!answer_body){
            alert("Fill out the answer first.")
            return
        }
        let resp = await fetch(`/api/v1/answer/${pk}/create`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrftoken'),
                "Content-Type": "application/json"
            },
            mode: "same-origin",
            cache: "no-cache",
            body: JSON.stringify({
                "body": answer_body
            })
        })
        if (resp.ok){
            return window.location.reload()
        }
        alert("There was an error with your form.")
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
            <h1 class="subtitle is-4">Have an answer?</h1>
            <div class="control">
                <textarea cols="30" rows="10" class="textarea" bind:value={answer_body}></textarea>
                <p class="help">{!!answer_body ? "" : "Fill out this field"}</p>
                <br>
                <button class="button is-info is-outlined" on:click={send_answer}>Post answer</button>
            </div>
        </div>
    {:catch error}
        <p>{error}</p>
    {/await}
</main>