<template>
    <div>
        <div class="row justify-content-center">
            <h1 class="title">명령어 벼락치기</h1>
        </div>
        <div class="row">
            <div class="col-12 text-right pb-4">
                <span class="mr-2"><i class="fas fa-angle-double-right mr-2"></i>10</span>
                <span class="mr-2"><i class="fas fa-question mr-2"></i>10 / 20</span>
                <span class="mr-2 text-success"><i class="fas fa-check mr-2"></i>10 / 20</span>
                <span class="mr-3 text-danger"><i class="fas fa-redo-alt mr-2"></i>10</span>
            </div>
        </div>
        <div class="row">
            <div class="col-12 px-5">
                <h4 class="text-center">라우터 또는 스위치에서 관리자 실행 모드로 진입하기 위해 사용하는 명령어는?</h4>
            </div>
        </div>
        <div class="row justify-content-center mt-5">
            <div class="col-10 col-sm-8 col-md-7 col-lg-6">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Answer">
                    <div class="input-group-append">
                        <input type="button" class="btn btn-outline-success" value="제출">
                    </div>
                </div>
            </div>
        </div>
        <div class="row justify-content-center mt-5">
            <div class="col-12 mb-3">
                <div class="card">
                    <div class="card-header">
                        Featured
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>
                        <li class="list-group-item">Vestibulum at eros</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "cramming-command"
};
</script>

<style scoped>
.title {
    padding: 60px 0 40px 0;
}
</style>
