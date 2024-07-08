<template>
    <div class="relative">
        <img src="@/assets/trphy.svg" class="lg:w-1/4 md:w-1/2 sm:w-5/6 w-5/6 mx-auto" alt="Icon description">      
        <div class="overflow-x-auto overflow-y-auto max-h-[600px] p-3">
            <table class=" text-md text-left rtl:text-right text-purple-100 mx-auto rounded-lg">
                <thead class="text-lg text-purple-100 bg-purple-700 ">
                    <tr>
                        <th scope="col" class="px-3 py-3">
                            Position
                        </th>
                        <th scope="col" class="px-3 py-3">
                            Driver
                        </th>
                        <th scope="col" class="px-3 py-3">
                            Car
                        </th>
                        <th scope="col" class="px-3 py-3">
                            Points
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="driver in leaderboardData" :key="driver.id"
                        class=" odd:bg-purple-800  even:bg-purple-600 border-b ">
                        <td class="px-3 py-4">{{ driver.position }}</td>
                        <td class="px-3 py-4">{{ driver.driver }}</td>
                        <td class="px-3 py-4">{{ driver.car }}</td>
                        <td class="px-3 py-4">{{ driver.points }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>


<script>
export default {
    props: {
        leaderboardData: {
            type: Array,
            required: true
        }
    }
}
</script>