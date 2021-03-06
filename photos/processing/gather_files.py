import luigi
import os

class GatherFiles(luigi.Task):
    input_path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(is_tmp=True)

    def run(self):
        with self.output().open('w') as f:
            for subdir, dirs, files in os.walk(self.input_path):
                for file in files:
                    f.write(os.path.join(subdir, file))
