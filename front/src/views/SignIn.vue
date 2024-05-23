<template>
<section class="h-screen bg-gray-800 text-white flex justify-center">
  <div class="w-3/4">
    <!-- Left column container with background-->
    <div
      class="flex h-full flex-wrap items-center justify-center lg:justify-between">
      <div
        class="shrink-1 mb-12 grow-0 basis-auto md:mb-0 md:w-9/12 md:shrink-0 lg:w-6/12 xl:w-6/12">
        <img
          src="https://tecdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
          class="w-full"
          alt="Sample image" />
      </div>

      <!-- Right column container -->
      <div class="mb-12 md:mb-0 md:w-8/12 lg:w-5/12 xl:w-5/12 ">
        <form class="">
          <!--Sign in section-->
          <div
            class="text-white flex flex-row items-center justify-center lg:justify-start border-slate-100 gap-5">
            <p class="mb-0 me-4 text-lg">Sign in with</p>

            <!-- Facebook -->
            <a href="https://www.facebook.com/" role="button">
                <!-- Facebook -->
                <span class="[&>svg]:h-7 [&>svg]:w-7 [&>svg]:fill-[#1877f2]">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
                    <!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                    <path
                        d="M80 299.3V512H196V299.3h86.5l18-97.8H196V166.9c0-51.7 20.3-71.5 72.7-71.5c16.3 0 29.4 .4 37 1.2V7.9C291.4 4 256.4 0 236.2 0C129.3 0 80 50.5 80 159.4v42.1H14v97.8H80z" />
                    </svg>
                </span>
                </a>
                    
                                <!-- X -->
                                <a href="#!" role="button">
                <!-- X -->
                <span class="[&>svg]:h-7 [&>svg]:w-7 [&>svg]:fill-black">
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 512 512">
                    <!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                    <path
                        d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z" />
                    </svg>
                </span>
                </a>
                    
                                <!-- Linkedin -->
                                <a href="#!" role="button">
                <!-- Google -->
                <span class="[&>svg]:h-7 [&>svg]:w-7 [&>svg]:fill-[#ea4335]">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 488 512">
                    <!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                    <path
                        d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z" />
                    </svg>
                </span>
                </a>
                            </div>

          <!-- Separator between social media sign in and email/password sign in -->
          <div
            class="my-4  before:mt-0.5 before:flex-1 before:border-t before:border-neutral-300 after:mt-0.5 after:flex-1 after:border-t after:border-neutral-300 dark:before:border-neutral-500 dark:after:border-neutral-500">
            <p
              class="mb-0 mx-4 text-left w-9/12 font-semibold dark:text-white">
              Or
            </p>
          </div>

          <!-- Email input -->
          <div class="relative mb-6" data-twe-input-wrapper-init>
            <input
              type="text"
              class="peer block min-h-[auto] w-full rounded bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[twe-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-white dark:placeholder:text-neutral-300 dark:autofill:shadow-autofill dark:peer-focus:text-primary [&:not([data-twe-input-placeholder-active])]:placeholder:opacity-0 border border-b-2 border-0"
              id="exampleFormControlInput2"
              placeholder="Email address" />
            <label
              for="exampleFormControlInput2"
              class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[2.15] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[1.15rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[twe-input-state-active]:-translate-y-[1.15rem] peer-data-[twe-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-400 dark:peer-focus:text-primary"
              >Username
            </label>
          </div>

          <!-- Password input -->
          <div class="relative mb-6" data-twe-input-wrapper-init>
            <input
              type="password"
              class="peer block min-h-[auto] w-full rounded bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[twe-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-white dark:placeholder:text-neutral-300 dark:autofill:shadow-autofill dark:peer-focus:text-primary [&:not([data-twe-input-placeholder-active])]:placeholder:opacity-0 border border-b-2 border-0"
              id="exampleFormControlInput22"
              placeholder="Password" />
            <label
              for="exampleFormControlInput22"
              class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[2.15] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[1.15rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[twe-input-state-active]:-translate-y-[1.15rem] peer-data-[twe-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-400 dark:peer-focus:text-primary"
              >Password
            </label>
          </div>

          <div class="text-white mb-6 flex items-center justify-between">
            <!--Forgot password link-->
            <a href="#!">Forgot password?</a>
          </div>

          <!-- Login button -->
          <div class="text-center lg:text-left">
                <button class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
<span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
Login
</span>
</button>

            <!-- Register link -->
            <p class="text-white mb-0 mt-2 pt-1 text-sm font-semibold ">
              Don't have an account?
              <a
                href="/signup"
                class="text-rose-700 text-danger transition duration-150 ease-in-out hover:text-danger-600 focus:text-danger-600 active:text-danger-700"
                >Register</a
              >
            </p>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
</template>
