use pyo3::prelude::*;
use sha2::{Sha256, Digest};
use rayon::prelude::*;

#[pyfunction]
fn find_arcana_nonce(target_prefix: String, range_start: u64, range_end: u64) -> PyResult<Option<u64>> {
    Python::with_gil(|py| {
        py.allow_threads(|| {
            let result = (range_start..range_end)
                .into_par_iter()
                .find_map_any(|nonce| {
                    let input = format!("{}{}", target_prefix, nonce);
                    let mut hasher = Sha256::new();
                    hasher.update(input.as_bytes());
                    let hash = hasher.finalize();

                    if hash[0] == 0 && hash[1] == 0 && (hash[2] & 0xf0) == 0 {
                        Some(nonce)
                    } else {
                        None
                    }
                });
            Ok(result)
        })
    })
}

#[pymodule]
fn prover_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(find_arcana_nonce, m)?)?;
    Ok(())
}
