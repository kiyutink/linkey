<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  const onChange = event => {
    dispatch("change", event);
  };
  export let value = "" + "";
</script>

<style lang="scss">
  input {
    height: 30px;
    padding: 5px;
    min-width: 200px;
    border-radius: 5px;
    border: 1px solid cornflowerblue;
    outline: none;

    &:focus {
      box-shadow: 0 0 0 1px cornflowerblue;
    }
  }
</style>

<input type="text" bind:value on:change={onChange} />
