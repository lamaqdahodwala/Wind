<script>
    import { send_gql_request } from './assets/assets.js'
    import { queries } from './assets/queries.js'

    export let pk

    async function load_question(){
        let resp = await send_gql_request()
        return resp['data']['singleQuestion']
    }
</script>

<p>
    The pk is {pk}
</p>