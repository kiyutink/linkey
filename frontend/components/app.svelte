<script>
  import { api } from "../lib/api";
  import Input from "./input.svelte";
  let url;
  let shortUrl;
</script>

<style lang="scss">
  main {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  h1 {
    font-weight: 500;
  }

  .container {
    width: 300px;
    display: flex;
    flex-direction: column;
  }

  button {
    margin-top: 5px;
    height: 30px;
    border-radius: 5px;
    border: 1px solid cornflowerblue;
    background-color: transparent;
    cursor: pointer;
    font-size: 18px;
    outline: none;

     &:focus {
      box-shadow: 0 0 0 1px cornflowerblue;
    }
  }
</style>

<main>
  <div class="container">
    <h1>Shorten your link</h1>

    <Input bind:value={url} />
    <button
      on:click={() => {
        api
          .createLink({ originalUrl: url, hasRedirection: false })
          .then(({ data }) => {
            shortUrl = data.shortUrl;
          });
      }}>
      Shorten
    </button>
  </div>

  {#if shortUrl}{shortUrl}{/if}
</main>
