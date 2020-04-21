from SLURMWorker import SLURMWorker

commands = "echo \"Testing SLURMWorker\""
script_file_name = "test.cfg"

worker = SLURMWorker()
worker.make_sbatch_script(
        script_file_name,
        "test_SLURMWorker",
        "kin.ho.lo@cern.ch",
        "1",
        "1gb",
        "00:05:00",
        "test_SLURMWorker",
        commands,
        )
worker.sbatch_submit(script_file_name)
