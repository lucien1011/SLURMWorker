import os

basic_script_text_template = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user={email}
#SBATCH --ntasks={ntasks}
#SBATCH --mem={mem}
#SBATCH --time={time}
#SBATCH --output={output}_%j.log
pwd; hostname; date

{commands}

date
"""

class SLURMWorker(object):
    def sbatch_submit(self,file_path):
        os.system("sbatch "+file_path)

    def make_sbatch_script(self,
            out_path,
            job_name,
            email,
            ntasks,
            mem,
            time,
            output,
            commands,
            ):
        script_file = open(out_path,"w")
        basic_script_text = basic_script_text_template.format(
                job_name = job_name,
                email = email,
                ntasks = ntasks,
                mem = mem,
                time = time,
                output = output,
                commands = commands,
                )
        script_file.write(basic_script_text)
        script_file.close()
