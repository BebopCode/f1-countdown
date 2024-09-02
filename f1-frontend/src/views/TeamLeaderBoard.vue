<template>
    <div class="my-5">
        <div class="overflow-x-auto overflow-y-auto max-h-[300px] p-3">
            <table class=" text-md text-left rtl:text-right text-black mx-auto rounded-lg">
                <thead class="text-xl text-black bg-slate-700 ">
                    <tr>
                        <th scope="col" class="px-5 py-3">
                            Position
                        </th>
                        <th scope="col" class="px-5 py-3">
                            Team
                        </th>
                        <th scope="col" class="px-5 py-3">
                            Points
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="team in teamLeaderboardData" :key="team.id"
                        class="text-lg odd:bg-slate-800  even:bg-slate-600 border-b ">
                        <td class="px-3 py-4">{{ team.position }}</td>
                        <td class="px-3 py-4">{{ team.team }}</td>
                        <td class="px-3 py-4">{{ team.points }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>


<script>
export default {
    props: {
        teamLeaderboardData: {
            type: Array,
            required: true
        }
    }
}
</script>