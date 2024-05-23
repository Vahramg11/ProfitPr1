<template>
    <div class="h-screen bg-gray-800 text-white flex justify-center">
        <form>
            <h1>Add Poll</h1>
            <br>
            <div class="relative mb-6" data-twe-input-wrapper-init>
            <input
              type="text"
              class="peer block min-h-[auto] rounded bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[twe-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-white dark:placeholder:text-neutral-300 dark:autofill:shadow-autofill dark:peer-focus:text-primary [&:not([data-twe-input-placeholder-active])]:placeholder:opacity-0 border border-b-2 border-0"
              id="exampleFormControlInput2"
              placeholder="Email address" />
            <label
              for="exampleFormControlInput2"
              class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[2.15] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[1.15rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[twe-input-state-active]:-translate-y-[1.15rem] peer-data-[twe-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-400 dark:peer-focus:text-primary"
              >question
            </label>
            </div>
            <div class="relative mb-6" data-twe-input-wrapper-init>
            <input
              type="text"
              class="peer block min-h-[auto] rounded bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[twe-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-white dark:placeholder:text-neutral-300 dark:autofill:shadow-autofill dark:peer-focus:text-primary [&:not([data-twe-input-placeholder-active])]:placeholder:opacity-0 border border-b-2 border-0"
              id="exampleFormControlInput2"
              placeholder="Email address" />
            <label
              for="exampleFormControlInput2"
              class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[2.15] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[1.15rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[twe-input-state-active]:-translate-y-[1.15rem] peer-data-[twe-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-400 dark:peer-focus:text-primary"
              >option
            </label>
            </div>
            <input type="checkbox" name="active" />
            <br>
            <button type="submit">Submit</button>
            <br>
            <button>Add Option</button>
        </form>
        
    </div>
</template>